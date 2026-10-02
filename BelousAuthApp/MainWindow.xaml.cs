using System;
using System.Linq;
using System.Text.RegularExpressions;
using System.Windows;
using System.Windows.Media;
using BelousAuthApp.Data;
using BelousAuthApp.Models;

namespace BelousAuthApp
{
    public partial class MainWindow : Window
    {
        private readonly AppDbContext context = new AppDbContext();

        public MainWindow()
        {
            InitializeComponent();
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            try
            {
                // Загрузка списка секретных вопросов из базы данных PostgreSQL через EF Core
                var questions = context.СекретныйВопрос
                    .Select(i => i.СекретныйВопрос1)
                    .ToList();

                qwest.ItemsSource = questions;
                if (questions.Count > 0)
                {
                    qwest.SelectedIndex = 0;
                }

                // Инициализация валидации пароля
                ValidatePassword();
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ошибка подключения к базе данных PostgreSQL:\n{ex.Message}\n\nУбедитесь, что служба PostgreSQL запущена и база user_auth_db создана.",
                    "Ошибка подключения", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void SignIn_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                // Проверка согласия с условиями
                if (chkAgree.IsChecked != true)
                {
                    MessageBox.Show("Для продолжения необходимо подтвердить согласие с условиями!", 
                        "Предупреждение", MessageBoxButton.OK, MessageBoxImage.Warning);
                    return;
                }

                // Проверка заполненности всех обязательных полей
                if (string.IsNullOrWhiteSpace(lName.Text) ||
                    string.IsNullOrWhiteSpace(name.Text) ||
                    string.IsNullOrWhiteSpace(eMail.Text) ||
                    string.IsNullOrWhiteSpace(passw.Password) ||
                    string.IsNullOrWhiteSpace(word.Text) ||
                    string.IsNullOrWhiteSpace(otvet.Text) ||
                    qwest.SelectedItem == null)
                {
                    MessageBox.Show("Все поля формы обязательны для заполнения!", 
                        "Ошибка валидации", MessageBoxButton.OK, MessageBoxImage.Warning);
                    return;
                }

                // Проверка корректности e-mail
                if (!Regex.IsMatch(eMail.Text.Trim(), @"^[^@\s]+@[^@\s]+\.[^@\s]+$"))
                {
                    MessageBox.Show("Укажите корректный адрес электронной почты (например, ivanov@gmail.com)!", 
                        "Ошибка валидации", MessageBoxButton.OK, MessageBoxImage.Warning);
                    return;
                }

                // Проверка длины пароля
                if (passw.Password.Length < 6)
                {
                    MessageBox.Show("Минимальная длина пароля должна составлять не менее 6 символов!", 
                        "Ошибка валидации пароля", MessageBoxButton.OK, MessageBoxImage.Warning);
                    return;
                }

                // Проверка совпадения паролей
                if (passw.Password != passwRepeat.Password)
                {
                    MessageBox.Show("Введенные пароли не совпадают!", 
                        "Ошибка валидации пароля", MessageBoxButton.OK, MessageBoxImage.Warning);
                    return;
                }

                // Поиск кода выбранного секретного вопроса в базе данных
                string selectedQuestionText = qwest.Text;
                int questionId = context.СекретныйВопрос
                    .Where(i => i.СекретныйВопрос1 == selectedQuestionText)
                    .Select(i => i.КодСекретногоВопроса)
                    .FirstOrDefault();

                if (questionId == 0)
                {
                    questionId = context.СекретныйВопрос
                        .Select(i => i.КодСекретногоВопроса)
                        .FirstOrDefault();
                }

                // Создание нового пользователя и сохранение в PostgreSQL (в точности по методичке)
                context.Пользователь.Add(new Пользователь
                {
                    Фамилия = lName.Text.Trim(),
                    Имя = name.Text.Trim(),
                    ЭлектроннаяПочта = eMail.Text.Trim(),
                    Пароль = passw.Password,
                    КодовоеСлово = word.Text.Trim(),
                    ОтветНаСекретныйВопрос = otvet.Text.Trim(),
                    КодСекретногоВопроса = questionId
                });

                context.SaveChanges();

                MessageBox.Show($"Пользователь {lName.Text} добавлен", "Успешная регистрация", 
                    MessageBoxButton.OK, MessageBoxImage.Information);

                // Открытие окна со списком зарегистрированных пользователей
                UserWin userWin = new UserWin();
                userWin.Show();
                this.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ошибка при сохранении пользователя в базу данных:\n{ex.Message}", 
                    "Ошибка сохранения", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void Passw_PasswordChanged(object sender, RoutedEventArgs e)
        {
            ValidatePassword();
        }

        private void PasswRepeat_PasswordChanged(object sender, RoutedEventArgs e)
        {
            ValidatePassword();
        }

        private void ValidatePassword()
        {
            string p1 = passw?.Password ?? string.Empty;
            string p2 = passwRepeat?.Password ?? string.Empty;

            var brushSuccess = new SolidColorBrush(Color.FromRgb(78, 201, 176)); // #4EC9B0 (зеленый)
            var brushMuted = new SolidColorBrush(Color.FromRgb(170, 170, 170));   // #AAAAAA (серый)
            var brushError = new SolidColorBrush(Color.FromRgb(244, 71, 71));     // #F44747 (красный)

            // Минимальная длина 6 символов
            bool isMinLength = p1.Length >= 6;
            if (tbRuleMinLength != null)
            {
                tbRuleMinLength.Foreground = isMinLength ? brushSuccess : new SolidColorBrush(Color.FromRgb(0, 122, 204));
                tbRuleMinLength.Text = isMinLength ? "✔ Минимальная длина 6 символов выполнена" : "Минимальная длина пароля 6 символов";
            }

            // Условие 1: Наличие цифр
            bool hasDigit = p1.Any(char.IsDigit);
            if (tbRule1 != null)
            {
                tbRule1.Foreground = hasDigit ? brushSuccess : brushMuted;
                tbRule1.Text = (hasDigit ? "✔ " : "") + "Условия пароля 1: наличие цифр";
            }

            // Условие 2: Наличие строчных букв
            bool hasLower = p1.Any(char.IsLower);
            if (tbRule2 != null)
            {
                tbRule2.Foreground = hasLower ? brushSuccess : brushMuted;
                tbRule2.Text = (hasLower ? "✔ " : "") + "Условия пароля 2: наличие строчных букв";
            }

            // Условие 3: Наличие заглавных букв
            bool hasUpper = p1.Any(char.IsUpper);
            if (tbRule3 != null)
            {
                tbRule3.Foreground = hasUpper ? brushSuccess : brushMuted;
                tbRule3.Text = (hasUpper ? "✔ " : "") + "Условия пароля 3: наличие заглавных букв";
            }

            // Условие 4: Совпадение паролей
            bool isMatch = !string.IsNullOrEmpty(p1) && p1 == p2;
            if (tbRule4 != null)
            {
                if (string.IsNullOrEmpty(p2))
                {
                    tbRule4.Foreground = brushMuted;
                    tbRule4.Text = "Условия пароля 4: совпадение паролей";
                }
                else
                {
                    tbRule4.Foreground = isMatch ? brushSuccess : brushError;
                    tbRule4.Text = (isMatch ? "✔ " : "✘ ") + "Условия пароля 4: совпадение паролей";
                }
            }
        }

        private void LName_GotFocus(object sender, RoutedEventArgs e)
        {
            if (lName.Text == "Иванов")
            {
                lName.SelectAll();
            }
        }

        private void Name_GotFocus(object sender, RoutedEventArgs e)
        {
            if (name.Text == "Иван")
            {
                name.SelectAll();
            }
        }

        private void Email_GotFocus(object sender, RoutedEventArgs e)
        {
            if (eMail.Text == "ivanov@gmail.com")
            {
                eMail.SelectAll();
            }
        }

        private void BtnViewUsers_Click(object sender, RoutedEventArgs e)
        {
            UserWin userWin = new UserWin();
            userWin.Show();
            this.Close();
        }
    }
}