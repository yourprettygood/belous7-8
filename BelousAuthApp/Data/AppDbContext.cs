using Microsoft.EntityFrameworkCore;
using BelousAuthApp.Models;

namespace BelousAuthApp.Data
{
    public class AppDbContext : DbContext
    {
        public DbSet<Пользователь> Пользователь { get; set; } = null!;
        public DbSet<СекретныйВопрос> СекретныйВопрос { get; set; } = null!;

        public static string DefaultConnectionString { get; set; } =
            "Host=127.0.0.1;Port=5432;Database=user_auth_db;Username=postgres;Password=postgres";

        public AppDbContext()
        {
        }

        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
        {
        }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                optionsBuilder.UseNpgsql(DefaultConnectionString);
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.Entity<СекретныйВопрос>(entity =>
            {
                entity.ToTable("СекретныйВопрос");
                entity.HasKey(e => e.КодСекретногоВопроса);
                entity.Property(e => e.КодСекретногоВопроса)
                    .HasColumnName("КодСекретногоВопроса")
                    .UseIdentityAlwaysColumn();

                entity.Property(e => e.СекретныйВопрос1)
                    .HasColumnName("СекретныйВопрос1")
                    .IsRequired()
                    .HasMaxLength(255);
            });

            modelBuilder.Entity<Пользователь>(entity =>
            {
                entity.ToTable("Пользователь");
                entity.HasKey(e => e.КодПользователя);
                entity.Property(e => e.КодПользователя)
                    .HasColumnName("КодПользователя")
                    .UseIdentityAlwaysColumn();

                entity.Property(e => e.Фамилия)
                    .HasColumnName("Фамилия")
                    .IsRequired()
                    .HasMaxLength(100);

                entity.Property(e => e.Имя)
                    .HasColumnName("Имя")
                    .IsRequired()
                    .HasMaxLength(100);

                entity.Property(e => e.ЭлектроннаяПочта)
                    .HasColumnName("ЭлектроннаяПочта")
                    .IsRequired()
                    .HasMaxLength(150);

                entity.Property(e => e.Пароль)
                    .HasColumnName("Пароль")
                    .IsRequired()
                    .HasMaxLength(255);

                entity.Property(e => e.КодовоеСлово)
                    .HasColumnName("КодовоеСлово")
                    .IsRequired()
                    .HasMaxLength(100);

                entity.Property(e => e.ОтветНаСекретныйВопрос)
                    .HasColumnName("ОтветНаСекретныйВопрос")
                    .IsRequired()
                    .HasMaxLength(255);

                entity.Property(e => e.КодСекретногоВопроса)
                    .HasColumnName("КодСекретногоВопроса");

                entity.HasOne(d => d.СекретныйВопрос)
                    .WithMany(p => p.Пользователи)
                    .HasForeignKey(d => d.КодСекретногоВопроса)
                    .OnDelete(DeleteBehavior.Restrict)
                    .HasConstraintName("FK_Пользователь_СекретныйВопрос");
            });
        }
    }
}
