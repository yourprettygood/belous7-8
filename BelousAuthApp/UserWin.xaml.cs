using System;
using System.Linq;
using System.Windows;
using Microsoft.EntityFrameworkCore;
using BelousAuthApp.Data;

namespace BelousAuthApp
{
    public partial class UserWin : Window
    {
        private readonly AppDbContext context = new AppDbContext();

        public UserWin()
        {
            InitializeComponent();
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            LoadUsers();
        }

        private void LoadUsers()
        {
            try
            {
                var users = context.Пользователь
                    .Include(u => u.СекретныйВопрос)
                    .OrderBy(u => u.КодПользователя)
                    .ToList();

                dgUsers.ItemsSource = users;
                tbStatus.Text = $"Всего пользователей: {users.Count}";
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ошибка при загрузке пользователей из базы данных: {ex.Message}",
                    "Ошибка", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void BtnRefresh_Click(object sender, RoutedEventArgs e)
        {
            LoadUsers();
        }

        private void BtnAddUser_Click(object sender, RoutedEventArgs e)
        {
            MainWindow regWin = new MainWindow();
            regWin.Show();
            this.Close();
        }
    }
}
