using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace BelousAuthApp.Models
{
    [Table("Пользователь")]
    public class Пользователь
    {
        [Key]
        [Column("КодПользователя")]
        public int КодПользователя { get; set; }

        [Required]
        [MaxLength(100)]
        [Column("Фамилия")]
        public string Фамилия { get; set; } = string.Empty;

        [Required]
        [MaxLength(100)]
        [Column("Имя")]
        public string Имя { get; set; } = string.Empty;

        [Required]
        [MaxLength(150)]
        [Column("ЭлектроннаяПочта")]
        public string ЭлектроннаяПочта { get; set; } = string.Empty;

        [Required]
        [MaxLength(255)]
        [Column("Пароль")]
        public string Пароль { get; set; } = string.Empty;

        [Required]
        [MaxLength(100)]
        [Column("КодовоеСлово")]
        public string КодовоеСлово { get; set; } = string.Empty;

        [Required]
        [MaxLength(255)]
        [Column("ОтветНаСекретныйВопрос")]
        public string ОтветНаСекретныйВопрос { get; set; } = string.Empty;

        [Column("КодСекретногоВопроса")]
        public int КодСекретногоВопроса { get; set; }

        [ForeignKey(nameof(КодСекретногоВопроса))]
        public virtual СекретныйВопрос? СекретныйВопрос { get; set; }
    }
}
