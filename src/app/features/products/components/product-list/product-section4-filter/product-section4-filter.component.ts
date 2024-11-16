import { Component } from '@angular/core';
import { ProductSettingFilterComponent } from "./product-setting-filter/product-setting-filter.component";
import { ProductShowComponent } from "./product-show/product-show.component";

@Component({
  selector: 'app-product-section4-filter',
  standalone: true,
  imports: [ProductSettingFilterComponent, ProductShowComponent],
  templateUrl: './product-section4-filter.component.html',
  styleUrl: './product-section4-filter.component.scss'
})
export class ProductSection4FilterComponent {

}
