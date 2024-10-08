import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ProductService } from '../../../../services/product.service';


@Component({
  selector: 'app-product-show',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-show.component.html',
  styleUrl: './product-show.component.scss',
  providers: [ProductService]  // Зарегистрируйте сервис как провайдера
})
export class ProductShowComponent {
  data: any[] = [];  // Переменная для хранения данных
  errorMessage: string | null = null;  // Переменная для хранения ошибки

  constructor(private productService: ProductService) {}

  // Метод для загрузки данных при нажатии на кнопку
  fetchData() {
    this.productService.fetchData().subscribe({
      next: (response: any) => {
        this.data = response;  // Сохраняем данные в переменную
        this.errorMessage = null;  // Очищаем ошибку, если данные успешно загружены
      },
      error: (error) => {
        this.errorMessage = 'Ошибка при загрузке данных';  // Сохраняем сообщение об ошибке
        console.error('Ошибка при загрузке данных:', error);
      }
    });
  }
}
