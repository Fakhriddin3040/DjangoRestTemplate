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
  errorMessage: string | null = null;

  constructor(private productService: MoyskladService) {}

  ngOnInit() {
    console.log('ProductShowComponent - Подписка на data$');
    this.productService.data$.subscribe({
      next: (data) => {
        console.log('ProductShowComponent - Полученные данные:', data);
        if (data && data.length > 0) {
          this.data = data;
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
}
