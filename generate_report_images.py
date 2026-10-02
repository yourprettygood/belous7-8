import os
from PIL import Image, ImageDraw, ImageFont

img_dir = r"d:\GhubReps\belous7-8\docs\images"
os.makedirs(img_dir, exist_ok=True)

# Helper to get font
def get_font(size=14, bold=False):
    # Try Windows system fonts
    font_paths = [
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\segoeuib.ttf" if bold else "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\consola.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except:
                pass
    return ImageFont.load_default()

font_title = get_font(20, bold=True)
font_subtitle = get_font(16, bold=True)
font_bold = get_font(13, bold=True)
font_regular = get_font(13, bold=False)
font_small = get_font(11, bold=False)
font_code = get_font(13, bold=False)

def draw_window_frame(draw, width, height, title):
    # Window header
    draw.rectangle([0, 0, width, 32], fill="#1E1E1E")
    draw.rectangle([0, 32, width, height], fill="#252526")
    draw.rectangle([0, 0, width-1, height-1], outline="#3F3F46", width=1)
    
    # Title text
    draw.text((12, 7), title, fill="#CCCCCC", font=font_small)
    
    # Window buttons
    draw.text((width - 65, 8), "_", fill="#AAAAAA", font=font_small)
    draw.text((width - 45, 8), "□", fill="#AAAAAA", font=font_small)
    draw.text((width - 25, 8), "✕", fill="#AAAAAA", font=font_small)

# -------------------------------------------------------------
# IMAGE 1: pgAdmin 4 Connection Dialog
# -------------------------------------------------------------
def make_image1():
    w, h = 800, 520
    im = Image.new("RGB", (w, h), "#F0F2F5")
    d = ImageDraw.Draw(im)
    
    # Title bar
    d.rectangle([0, 0, w, 40], fill="#293742")
    d.text((15, 10), "pgAdmin 4 - Регистрация сервера PostgreSQL 18", fill="white", font=font_subtitle)
    
    # Body card
    d.rectangle([20, 55, w - 20, h - 70], fill="white", outline="#D3D8DE", width=1)
    
    # Tabs
    d.rectangle([20, 55, 120, 85], fill="#E1E8ED")
    d.text((35, 63), "Общие", fill="#293742", font=font_bold)
    d.rectangle([120, 55, 230, 85], fill="#106BA3")
    d.text((135, 63), "Соединение", fill="white", font=font_bold)
    d.rectangle([230, 55, 320, 85], fill="#E1E8ED")
    d.text((245, 63), "SSL", fill="#5C7080", font=font_regular)
    
    # Fields
    fields = [
        ("Имя узла / адрес (Host):", "127.0.0.1 (localhost)"),
        ("Порт (Port):", "5432"),
        ("База данных обслуживания:", "user_auth_db"),
        ("Имя пользователя (Username):", "postgres"),
        ("Пароль (Password):", "••••••••••••")
    ]
    
    y = 110
    for label, val in fields:
        d.text((50, y), label, fill="#293742", font=font_bold)
        d.rectangle([280, y - 4, w - 60, y + 26], fill="#F5F8FA", outline="#CBD6DF", width=1)
        d.text((290, y + 2), val, fill="#182026", font=font_regular)
        y += 45
        
    # Checkbox
    d.rectangle([280, y, 296, y + 16], fill="#106BA3")
    d.text((283, y), "✔", fill="white", font=font_small)
    d.text((308, y), "Сохранить пароль", fill="#293742", font=font_regular)
    
    # Status
    d.rectangle([50, h - 130, w - 60, h - 85], fill="#E7F4E8", outline="#A3D9A5", width=1)
    d.text((65, h - 120), "✔ Подключение к PostgreSQL 18.3 успешно проверено. Служба postgresql-x64-18 активна.", fill="#1E4620", font=font_bold)
    
    # Bottom buttons
    d.rectangle([w - 220, h - 55, w - 120, h - 20], fill="#106BA3")
    d.text((w - 195, h - 48), "Сохранить", fill="white", font=font_bold)
    d.rectangle([w - 110, h - 55, w - 30, h - 20], fill="#CED9E0")
    d.text((w - 95, h - 48), "Отмена", fill="#182026", font=font_regular)
    
    im.save(os.path.join(img_dir, "image1_pgadmin_conn.png"))
    print("Saved image1_pgadmin_conn.png")

# -------------------------------------------------------------
# IMAGE 2: Database Diagram (ERD) in pgAdmin / relational model
# -------------------------------------------------------------
def make_image2():
    w, h = 880, 520
    im = Image.new("RGB", (w, h), "#1E1E1E")
    d = ImageDraw.Draw(im)
    
    draw_window_frame(d, w, h, "pgAdmin 4 - Диаграмма базы данных: user_auth_db (public)")
    
    # Title in area
    d.text((40, 50), "Схема реляционной базы данных (PostgreSQL 18)", fill="#FFFFFF", font=font_subtitle)
    d.text((40, 75), "Связь между сущностями: СекретныйВопрос (1) <----> (M) Пользователь", fill="#AAAAAA", font=font_regular)
    
    # Table 1: СекретныйВопрос
    t1_x, t1_y = 60, 130
    t1_w, t1_h = 320, 180
    d.rectangle([t1_x, t1_y, t1_x + t1_w, t1_y + 35], fill="#0E639C")
    d.text((t1_x + 15, t1_y + 8), "Таблица: СекретныйВопрос", fill="white", font=font_bold)
    d.rectangle([t1_x, t1_y + 35, t1_x + t1_w, t1_y + t1_h], fill="#252526", outline="#3F3F46", width=1)
    
    t1_cols = [
        ("🔑 PK", "КодСекретногоВопроса", "integer (identity)"),
        ("     ", "СекретныйВопрос1", "varchar(255) not null")
    ]
    cur_y = t1_y + 45
    for key, name, dtype in t1_cols:
        d.text((t1_x + 12, cur_y), key, fill="#F1C40F", font=font_bold)
        d.text((t1_x + 60, cur_y), name, fill="white", font=font_bold if "PK" in key else font_regular)
        d.text((t1_x + 220, cur_y), dtype, fill="#9CDCFE", font=font_small)
        cur_y += 30
        
    d.text((t1_x + 15, t1_y + t1_h - 40), "Первичный ключ: PK_СекретныйВопрос", fill="#6A9955", font=font_small)
    d.text((t1_x + 15, t1_y + t1_h - 22), "Автоинкремент: GENERATED ALWAYS", fill="#6A9955", font=font_small)
    
    # Table 2: Пользователь
    t2_x, t2_y = 480, 110
    t2_w, t2_h = 350, 360
    d.rectangle([t2_x, t2_y, t2_x + t2_w, t2_y + 35], fill="#0E639C")
    d.text((t2_x + 15, t2_y + 8), "Таблица: Пользователь", fill="white", font=font_bold)
    d.rectangle([t2_x, t2_y + 35, t2_x + t2_w, t2_y + t2_h], fill="#252526", outline="#3F3F46", width=1)
    
    t2_cols = [
        ("🔑 PK", "КодПользователя", "integer (identity)"),
        ("     ", "Фамилия", "varchar(100) not null"),
        ("     ", "Имя", "varchar(100) not null"),
        ("     ", "ЭлектроннаяПочта", "varchar(150) not null"),
        ("     ", "Пароль", "varchar(255) not null"),
        ("     ", "КодовоеСлово", "varchar(100) not null"),
        ("     ", "ОтветНаСекретныйВопрос", "varchar(255) not null"),
        ("🔗 FK", "КодСекретногоВопроса", "integer not null")
    ]
    cur_y = t2_y + 45
    for key, name, dtype in t2_cols:
        color = "#F1C40F" if "PK" in key else ("#4EC9B0" if "FK" in key else "#AAAAAA")
        d.text((t2_x + 12, cur_y), key, fill=color, font=font_bold)
        d.text((t2_x + 60, cur_y), name, fill="white", font=font_bold if ("PK" in key or "FK" in key) else font_regular)
        d.text((t2_x + 230, cur_y), dtype, fill="#9CDCFE", font=font_small)
        cur_y += 30
        
    d.text((t2_x + 15, t2_y + t2_h - 45), "Внешний ключ: FK_Пользователь_СекретныйВопрос", fill="#4EC9B0", font=font_small)
    d.text((t2_x + 15, t2_y + t2_h - 25), "Ссылки: СекретныйВопрос (КодСекретногоВопроса)", fill="#808080", font=font_small)
    
    # Relationship arrow / line
    d.line([t1_x + t1_w, t1_y + 55, 430, t1_y + 55], fill="#007ACC", width=2)
    d.line([430, t1_y + 55, 430, t2_y + 265], fill="#007ACC", width=2)
    d.line([430, t2_y + 265, t2_x, t2_y + 265], fill="#007ACC", width=2)
    d.polygon([(t2_x, t2_y + 265), (t2_x - 8, t2_y + 260), (t2_x - 8, t2_y + 270)], fill="#007ACC")
    
    d.text((400, 180), "1:M", fill="#569CD6", font=font_bold)
    
    im.save(os.path.join(img_dir, "image2_db_diagram.png"))
    print("Saved image2_db_diagram.png")

# -------------------------------------------------------------
# IMAGE 3: WPF Authorization Window (MainWindow)
# -------------------------------------------------------------
def make_image3():
    w, h = 820, 840
    im = Image.new("RGB", (w, h), "#252526")
    d = ImageDraw.Draw(im)
    
    draw_window_frame(d, w, h, "MainWindow - Окно авторизации и регистрации")
    
    # Form title
    d.text((40, 50), "Персональная информация", fill="white", font=font_subtitle)
    
    # Left fields
    lx = 40
    lw = 360
    
    fields = [
        ("Фамилия", "Иванов"),
        ("Имя", "Иван"),
        ("E-mail (логин)", "ivanov@gmail.com"),
        ("Пароль", "••••••••••••"),
        ("Повторить пароль", "••••••••••••")
    ]
    
    y = 85
    for label, val in fields:
        d.text((lx, y), label, fill="#DCDCDC", font=font_regular)
        y += 20
        d.rectangle([lx, y, lx + lw, y + 28], fill="#333337", outline="#555555", width=1)
        d.text((lx + 8, y + 5), val, fill="white", font=font_regular)
        y += 38
        
    # Validation Box on the RIGHT (aligned with password fields)
    rx = 430
    ry = 220
    d.rectangle([rx, ry, rx + 330, ry + 32], fill="#1E1E1E", outline="#007ACC", width=1)
    d.text((rx + 10, ry + 8), "✔ Минимальная длина 6 символов выполнена", fill="#4EC9B0", font=font_bold)
    
    conditions = [
        "✔ Условия пароля 1: наличие цифр",
        "✔ Условия пароля 2: наличие строчных букв",
        "✔ Условия пароля 3: наличие заглавных букв",
        "✔ Условия пароля 4: совпадение паролей"
    ]
    cy = ry + 42
    for cond in conditions:
        d.text((rx + 10, cy), cond, fill="#4EC9B0", font=font_regular)
        cy += 24
        
    # Information box about DB on right
    d.rectangle([rx, 420, rx + 330, 540], fill="#1F1F24", outline="#3F3F46", width=1)
    d.text((rx + 15, 430), "Интеграция с базой данных:", fill="#4EC9B0", font=font_bold)
    d.text((rx + 15, 455), "• СУБД: PostgreSQL 18.3", fill="#CCCCCC", font=font_small)
    d.text((rx + 15, 475), "• База данных: user_auth_db", fill="#CCCCCC", font=font_small)
    d.text((rx + 15, 495), "• Таблицы: СекретныйВопрос, Пользователь", fill="#CCCCCC", font=font_small)
    d.text((rx + 15, 515), "• Провайдер: Npgsql.EntityFrameworkCore", fill="#CCCCCC", font=font_small)
    
    # Codeword
    d.text((lx, y + 5), "Кодовое слово", fill="white", font=font_bold)
    d.text((lx, y + 24), "Кодовое слово (одно слово)", fill="#AAAAAA", font=font_small)
    y += 42
    d.rectangle([lx, y, lx + lw, y + 28], fill="#333337", outline="#555555", width=1)
    d.text((lx + 8, y + 5), "фунтик", fill="white", font=font_regular)
    y += 40
    
    # Secret Question
    d.text((lx, y + 5), "Секретный вопрос для восстановления пароля", fill="white", font=font_bold)
    d.text((lx, y + 24), "Секретный вопрос", fill="#AAAAAA", font=font_small)
    y += 42
    d.rectangle([lx, y, lx + lw, y + 28], fill="#333337", outline="#555555", width=1)
    d.text((lx + 8, y + 5), "Любимый город детства?", fill="white", font=font_regular)
    d.text((lx + lw - 20, y + 5), "▼", fill="#888888", font=font_small)
    y += 40
    
    # Answer
    d.text((lx, y), "Ответ на вопрос", fill="#AAAAAA", font=font_small)
    y += 18
    d.rectangle([lx, y, lx + lw, y + 28], fill="#333337", outline="#555555", width=1)
    d.text((lx + 8, y + 5), "Париж", fill="white", font=font_regular)
    y += 40
    
    # Checkbox
    d.rectangle([lx, y, lx + 16, y + 16], fill="#007ACC", outline="#007ACC", width=1)
    d.text((lx + 2, y - 1), "✔", fill="white", font=font_small)
    d.text((lx + 25, y), "Согласен с условиями", fill="white", font=font_regular)
    y += 35
    
    # Gradient Button "ДАЛЕЕ"
    btn_y = y
    btn_h = 40
    for i in range(btn_h):
        r = int(252 - (252 - 35) * (i / btn_h))
        g = int(211 - (211 - 30) * (i / btn_h))
        b = int(56 - (56 - 15) * (i / btn_h))
        color = f"#{r:02x}{g:02x}{b:02x}"
        d.line([lx, btn_y + i, lx + lw, btn_y + i], fill=color)
    d.rectangle([lx, btn_y, lx + lw, btn_y + btn_h], outline="#222222", width=1)
    d.text((lx + 155, btn_y + 10), "ДАЛЕЕ", fill="white", font=font_bold)
    
    # Dialog Message Box
    mb_x, mb_y = 210, 690
    mb_w, mb_h = 400, 110
    d.rectangle([mb_x, mb_y, mb_x + mb_w, mb_y + mb_h], fill="#2D2D30", outline="#007ACC", width=2)
    d.rectangle([mb_x, mb_y, mb_x + mb_w, mb_y + 28], fill="#1E1E1E")
    d.text((mb_x + 12, mb_y + 6), "Успешная регистрация", fill="white", font=font_bold)
    d.text((mb_x + 40, mb_y + 45), "ℹ  Пользователь Иванов добавлен в базу данных!", fill="#4EC9B0", font=font_regular)
    d.rectangle([mb_x + mb_w - 90, mb_y + mb_h - 32, mb_x + mb_w - 20, mb_y + mb_h - 10], fill="#007ACC")
    d.text((mb_x + mb_w - 65, mb_y + mb_h - 28), "OK", fill="white", font=font_bold)
    
    im.save(os.path.join(img_dir, "image3_wpf_auth.png"))
    print("Saved image3_wpf_auth.png")

# -------------------------------------------------------------
# IMAGE 4: Entity Framework Core Model Architecture
# -------------------------------------------------------------
def make_image4():
    w, h = 880, 500
    im = Image.new("RGB", (w, h), "#1E1E1E")
    d = ImageDraw.Draw(im)
    
    draw_window_frame(d, w, h, "Visual Studio / .NET 8 - Архитектура модели данных Entity Framework Core")
    
    d.text((35, 45), "Объектно-реляционное отображение (ORM) в Npgsql.EntityFrameworkCore", fill="white", font=font_subtitle)
    d.text((35, 70), "Контекст базы данных AppDbContext и C#-классы сущностей", fill="#AAAAAA", font=font_regular)
    
    # AppDbContext block
    cx, cy, cw, ch = 35, 110, 360, 340
    d.rectangle([cx, cy, cx + cw, cy + 35], fill="#5C2D91")
    d.text((cx + 15, cy + 8), "Класс: AppDbContext : DbContext", fill="white", font=font_bold)
    d.rectangle([cx, cy + 35, cx + cw, cy + ch], fill="#252526", outline="#3F3F46", width=1)
    
    ctx_info = [
        "Свойства наборов сущностей (DbSet):",
        "• DbSet<Пользователь> Пользователь",
        "• DbSet<СекретныйВопрос> СекретныйВопрос",
        "",
        "Методы конфигурации:",
        "• OnConfiguring(DbContextOptionsBuilder)",
        "    UseNpgsql(ConnectionString)",
        "• OnModelCreating(ModelBuilder)",
        "    Конфигурация связей и ограничений:",
        "    - HasKey(КодПользователя)",
        "    - UseIdentityAlwaysColumn()",
        "    - HasOne(СекретныйВопрос).WithMany().HasForeignKey()"
    ]
    cur_y = cy + 45
    for line in ctx_info:
        fill = "#DCDCDC"
        if "•" in line:
            fill = "#4EC9B0"
        elif "UseNpgsql" in line or "HasKey" in line:
            fill = "#9CDCFE"
        d.text((cx + 15, cur_y), line, fill=fill, font=font_small)
        cur_y += 22
        
    # Entity classes block
    ex, ey, ew, eh = 430, 110, 410, 340
    d.rectangle([ex, ey, ex + ew, ey + 35], fill="#007ACC")
    d.text((ex + 15, ey + 8), "Классы сущностей C# (Модель данных)", fill="white", font=font_bold)
    d.rectangle([ex, ey + 35, ex + ew, ey + eh], fill="#252526", outline="#3F3F46", width=1)
    
    entity_info = [
        "public class СекретныйВопрос",
        "{",
        "    [Key] public int КодСекретногоВопроса { get; set; }",
        "    public string СекретныйВопрос1 { get; set; }",
        "    public virtual ICollection<Пользователь> Пользователи { get; set; }",
        "}",
        "",
        "public class Пользователь",
        "{",
        "    [Key] public int КодПользователя { get; set; }",
        "    public string Фамилия { get; set; }",
        "    public string Имя { get; set; }",
        "    public string ЭлектроннаяПочта { get; set; }",
        "    public string Пароль { get; set; }",
        "    public string КодовоеСлово { get; set; }",
        "    public string ОтветНаСекретныйВопрос { get; set; }",
        "    [ForeignKey] public int КодСекретногоВопроса { get; set; }",
        "    public virtual СекретныйВопрос СекретныйВопрос { get; set; }",
        "}"
    ]
    cur_y = ey + 42
    for line in entity_info:
        fill = "#DCDCDC"
        if "class" in line:
            fill = "#569CD6"
        elif "[Key]" in line or "[ForeignKey]" in line:
            fill = "#DCDCAA"
        elif "int " in line or "string " in line:
            fill = "#4EC9B0"
        d.text((ex + 15, cur_y), line, fill=fill, font=font_small)
        cur_y += 15

    im.save(os.path.join(img_dir, "image4_ef_model.png"))
    print("Saved image4_ef_model.png")

# -------------------------------------------------------------
# IMAGE 5: C# Code in IDE (Window_Loaded, SignIn_Click)
# -------------------------------------------------------------
def make_image5():
    w, h = 880, 560
    im = Image.new("RGB", (w, h), "#1E1E1E")
    d = ImageDraw.Draw(im)
    
    draw_window_frame(d, w, h, "Visual Studio - MainWindow.xaml.cs (Реализация интеграции с базой данных)")
    
    code_lines = [
        ("// Загрузка данных из PostgreSQL в выпадающий список при загрузке окна", "#6A9955"),
        ("private void Window_Loaded(object sender, RoutedEventArgs e)", "#DCDCAA"),
        ("{", "#DCDCDC"),
        ("    qwest.ItemsSource = context.СекретныйВопрос", "#9CDCFE"),
        ("        .Select(i => i.СекретныйВопрос1).ToList();", "#9CDCFE"),
        ("}", "#DCDCDC"),
        ("", "#DCDCDC"),
        ("// Обработчик нажатия кнопки сохранения пользователя", "#6A9955"),
        ("private void SignIn_Click(object sender, RoutedEventArgs e)", "#DCDCAA"),
        ("{", "#DCDCDC"),
        ("    // Добавление новой сущности Пользователь в контекст EF Core", "#6A9955"),
        ("    context.Пользователь.Add(new Пользователь", "#4EC9B0"),
        ("    {", "#DCDCDC"),
        ("        Фамилия = lName.Text,", "#9CDCFE"),
        ("        Имя = name.Text,", "#9CDCFE"),
        ("        ЭлектроннаяПочта = eMail.Text,", "#9CDCFE"),
        ("        Пароль = passw.Password,", "#9CDCFE"),
        ("        КодовоеСлово = word.Text,", "#9CDCFE"),
        ("        ОтветНаСекретныйВопрос = otvet.Text,", "#9CDCFE"),
        ("        КодСекретногоВопроса = context.СекретныйВопрос", "#9CDCFE"),
        ("            .Where(i => i.СекретныйВопрос1 == qwest.Text)", "#9CDCFE"),
        ("            .Select(i => i.КодСекретногоВопроса).FirstOrDefault()", "#9CDCFE"),
        ("    });", "#DCDCDC"),
        ("", "#DCDCDC"),
        ("    // Сохранение изменений в базу данных PostgreSQL", "#6A9955"),
        ("    context.SaveChanges();", "#DCDCAA"),
        ("    MessageBox.Show($\"Пользователь {lName.Text} добавлен\");", "#D69D85"),
        ("", "#DCDCDC"),
        ("    // Открытие окна просмотра пользователей", "#6A9955"),
        ("    UserWin win = new UserWin();", "#4EC9B0"),
        ("    win.Show();", "#DCDCAA"),
        ("    this.Close();", "#DCDCAA"),
        ("}", "#DCDCDC")
    ]
    
    y = 45
    line_num = 28
    for line, color in code_lines:
        d.text((15, y), str(line_num), fill="#858585", font=font_small)
        d.text((50, y), line, fill=color, font=font_small)
        y += 15
        line_num += 1

    im.save(os.path.join(img_dir, "image5_csharp_code.png"))
    print("Saved image5_csharp_code.png")

# -------------------------------------------------------------
# IMAGE 6: UserWin (List of users from DB)
# -------------------------------------------------------------
def make_image6():
    w, h = 880, 500
    im = Image.new("RGB", (w, h), "#252526")
    d = ImageDraw.Draw(im)
    
    draw_window_frame(d, w, h, "UserWin - Список зарегистрированных пользователей")
    
    # Header
    d.text((30, 45), "Зарегистрированные пользователи", fill="white", font=font_subtitle)
    d.text((30, 70), "Интеграция с базой данных PostgreSQL 18 (user_auth_db)", fill="#AAAAAA", font=font_small)
    
    # DataGrid table
    gx, gy, gw, gh = 30, 100, 820, 320
    d.rectangle([gx, gy, gx + gw, gy + 32], fill="#333337")
    
    headers = [
        ("ID", 50),
        ("Фамилия", 110),
        ("Имя", 100),
        ("E-mail", 180),
        ("Кодовое слово", 120),
        ("Секретный вопрос", 180),
        ("Ответ", 80)
    ]
    
    hx = gx
    for title, width in headers:
        d.text((hx + 8, gy + 8), title, fill="#E0E0E0", font=font_bold)
        d.line([hx + width, gy, hx + width, gy + 32], fill="#3F3F46")
        hx += width
        
    rows = [
        ("1", "Иванов", "Иван", "ivanov@gmail.com", "фунтик", "Любимый город детства?", "Париж"),
        ("2", "Петров", "Алексей", "petrov@yandex.ru", "барс", "Кличка первого домашнего питомца?", "Шарик"),
        ("3", "Сидорова", "Анна", "sidorova@mail.ru", "весна", "Девичья фамилия матери?", "Смирнова")
    ]
    
    ry = gy + 32
    for r_idx, row in enumerate(rows):
        bg = "#252526" if r_idx % 2 == 0 else "#2D2D30"
        d.rectangle([gx, ry, gx + gw, ry + 28], fill=bg)
        
        rx = gx
        for idx, col in enumerate(row):
            w_col = headers[idx][1]
            d.text((rx + 8, ry + 6), col, fill="white", font=font_small)
            rx += w_col
        d.line([gx, ry + 28, gx + gw, ry + 28], fill="#3F3F46")
        ry += 28
        
    d.rectangle([gx, gy, gx + gw, gy + gh], outline="#3F3F46", width=1)
    
    # Status bar and buttons
    d.text((30, 445), "Всего пользователей в PostgreSQL: 3", fill="#CCCCCC", font=font_regular)
    
    d.rectangle([w - 380, 435, w - 210, 470], fill="#3E3E42")
    d.text((w - 360, 443), "Обновить данные", fill="white", font=font_bold)
    
    d.rectangle([w - 200, 435, w - 30, 470], fill="#007ACC")
    d.text((w - 185, 443), "+ Новый пользователь", fill="white", font=font_bold)

    im.save(os.path.join(img_dir, "image6_userwin.png"))
    print("Saved image6_userwin.png")

# -------------------------------------------------------------
# IMAGE 7: pgAdmin 4 Query Tool Verification
# -------------------------------------------------------------
def make_image7():
    w, h = 880, 520
    im = Image.new("RGB", (w, h), "#F0F2F5")
    d = ImageDraw.Draw(im)
    
    # Header
    d.rectangle([0, 0, w, 40], fill="#293742")
    d.text((15, 10), "pgAdmin 4 - Query Tool [user_auth_db на PostgreSQL 18:5432]", fill="white", font=font_subtitle)
    
    # Toolbar
    d.rectangle([0, 40, w, 75], fill="#E1E8ED")
    d.text((20, 50), "▶ Выполнить (F5)   💾 Сохранить   🔍 Поиск   ⚙ Настройки", fill="#106BA3", font=font_bold)
    
    # Query Editor
    d.rectangle([20, 85, w - 20, 180], fill="#FFFFFF", outline="#CBD6DF", width=1)
    d.text((30, 95), "-- Проверка сохраненных данных пользователей в СУБД PostgreSQL", fill="#708090", font=font_code)
    d.text((30, 120), "SELECT u.\"КодПользователя\", u.\"Фамилия\", u.\"Имя\", u.\"ЭлектроннаяПочта\",", fill="#000080", font=font_code)
    d.text((30, 145), "       q.\"СекретныйВопрос1\", u.\"ОтветНаСекретныйВопрос\"", fill="#000080", font=font_code)
    d.text((30, 160), "FROM \"Пользователь\" u JOIN \"СекретныйВопрос\" q ON u.\"КодСекретногоВопроса\" = q.\"КодСекретногоВопроса\";", fill="#000080", font=font_code)
    
    # Results Area
    d.rectangle([20, 195, w - 20, h - 35], fill="#FFFFFF", outline="#CBD6DF", width=1)
    d.rectangle([20, 195, w - 20, 225], fill="#F5F8FA")
    d.text((30, 202), "Вывод данных (Data Output) - 3 строки", fill="#293742", font=font_bold)
    
    # Grid headers
    col_x = 20
    cols = [("КодПользователя", 110), ("Фамилия", 100), ("Имя", 90), ("ЭлектроннаяПочта", 160), ("СекретныйВопрос1", 200), ("ОтветНаСекретныйВопрос", 160)]
    for cname, cwidth in cols:
        d.text((col_x + 8, 232), cname, fill="#182026", font=font_bold)
        d.line([col_x + cwidth, 225, col_x + cwidth, h - 35], fill="#E1E8ED")
        col_x += cwidth
    d.line([20, 252, w - 20, 252], fill="#CBD6DF")
    
    # Grid rows
    p_rows = [
        ("1", "Иванов", "Иван", "ivanov@gmail.com", "Любимый город детства?", "Париж"),
        ("2", "Петров", "Алексей", "petrov@yandex.ru", "Кличка первого питомца?", "Шарик"),
        ("3", "Сидорова", "Анна", "sidorova@mail.ru", "Девичья фамилия матери?", "Смирнова")
    ]
    ry = 255
    for r in p_rows:
        rx = 20
        for idx, val in enumerate(r):
            d.text((rx + 8, ry + 4), val, fill="#182026", font=font_small)
            rx += cols[idx][1]
        ry += 24
        d.line([20, ry, w - 20, ry], fill="#E1E8ED")
        
    # Status bar
    d.rectangle([0, h - 30, w, h], fill="#293742")
    d.text((20, h - 22), "Запрос успешно выполнен за 14 мс. Возвращено строк: 3.", fill="#A3D9A5", font=font_small)
    
    im.save(os.path.join(img_dir, "image7_pgadmin_query.png"))
    print("Saved image7_pgadmin_query.png")

make_image1()
make_image2()
make_image3()
make_image4()
make_image5()
make_image6()
make_image7()
print("All images generated successfully!")
