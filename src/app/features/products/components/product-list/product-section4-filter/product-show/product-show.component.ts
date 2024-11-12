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
  
})
export class ProductShowComponent implements OnInit  {
  data: any[] = [];
  imageUrl: string | null = null;
  errorMessage: string | null = null;

  constructor(private productService: MoyskladService) {}

  ngOnInit() {
    console.log('ProductShowComponent - Подписка на data$');
    this.loadProductData();
    // this.loadProductImage();
    this.productService.data$.subscribe({
      next: (data) => {
        console.log('ProductShowComponent - Полученные данные:', data);
        if (data && data.length > 0) {
          this.data = data.slice(0, 10); // Получаем только первые 10 объектов
          console.log('ProductShowComponent - Первые 10 данных:', this.data);
        } else {
          console.warn('ProductShowComponent - Нет данных для отображения');
        }
      },
      error: (error) => {
        this.errorMessage = 'Ошибка при загрузке данных';
        console.error('ProductShowComponent - Ошибка при подписке на данные:', error);
      }
    });
  }


  loadProductData() {
    this.productService.fetchData().subscribe({
      next: (data) => {
        if (data && data.length > 0) {
          data.forEach((element: any) => {
            
            const blob = new Blob([new Uint8Array(element.imageBuffer.data)], {type : 'image/png'});
            element.imageBlobUrl = URL.createObjectURL(blob)
          });
          this.data = data.slice(0, 10);
        }
      },
      error: (error) => {
        this.errorMessage = 'Ошибка при загрузке данных';
      }
    });
  }  
}
