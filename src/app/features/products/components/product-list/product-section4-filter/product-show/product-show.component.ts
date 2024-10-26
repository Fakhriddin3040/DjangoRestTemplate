import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { MoyskladService } from '../../../../../../services/moysklad.service';



@Component({
  selector: 'app-product-show',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-show.component.html',
  styleUrls: ['./product-show.component.scss'],
  providers: [MoyskladService]  // Зарегистрируйте сервис как провайдера
})
export class ProductShowComponent implements OnInit  {
  data: any[] = [];
  errorMessage: string | null = null;

  constructor(private productService: MoyskladService) {}

  ngOnInit() {
  // Подписываемся на поток данных
  this.productService.data$.subscribe({
    next: (data) => {
      console.log('Полученные данные в ProductShowComponent:', data); // Лог данных для проверки
      if (data && data.length > 0) {
        this.data = data; // Сохраняем данные для отображения
      } else {
        console.warn('Нет данных для отображения в ProductShowComponent'); // Лог, если данные пустые
      }
    },
    error: (error) => {
      this.errorMessage = 'Ошибка при загрузке данных';
      console.error('Ошибка при подписке на данные:', error);
    }
  });


  }
}
