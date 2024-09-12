import { Component } from '@angular/core';
import { ContainerComponent } from '../../shared/container/container.component';
import { Section1ProductSlideComponent } from "./section1-product-slide/section1-product-slide.component";
import { Section2OurAdvantagesComponent } from "./section2-our-advantages/section2-our-advantages.component";
import { Section3SaleComponent } from "./section3-sale/section3-sale.component";
import { Section4ShowReverseTimeSaleComponent } from "./section4-show-reverse-time-sale/section4-show-reverse-time-sale.component";
import { Section5SlideSaleComponent } from "./section5-slide-sale/section5-slide-sale.component";
import { Section6ClothingApparelComponent } from "./section6-clothing-apparel/section6-clothing-apparel.component";

@Component({
  selector: 'app-main',
  standalone: true,
  imports: [
    ContainerComponent,
    Section1ProductSlideComponent,
    Section2OurAdvantagesComponent,
    Section3SaleComponent,
    Section4ShowReverseTimeSaleComponent,
    Section5SlideSaleComponent,
    Section6ClothingApparelComponent
],
  templateUrl: './main.component.html',
  styleUrl: './main.component.scss'
})
export class MainComponent {

}
