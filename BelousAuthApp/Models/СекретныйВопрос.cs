using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace BelousAuthApp.Models
{
    [Table("СекретныйВопрос")]
    public class СекретныйВопрос
    {
        [Key]
        [Column("КодСекретногоВопроса")]
        public int КодСекретногоВопроса { get; set; }

        [Required]
        [MaxLength(255)]
        [Column("СекретныйВопрос1")]
        public string СекретныйВопрос1 { get; set; } = string.Empty;

        public virtual ICollection<Пользователь> Пользователи { get; set; } = new List<Пользователь>();

        public override string ToString() => СекретныйВопрос1;
    }
}
