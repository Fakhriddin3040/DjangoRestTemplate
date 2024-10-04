import { Component } from '@angular/core';
import { BreadcrumbNavigationComponent } from "../../../../shared/components/breadcrumb-navigation/breadcrumb-navigation.component";
import { ContainerComponent } from "../../../../shared/container/container.component";
import { Routes, RouterOutlet } from '@angular/router';
import { ProductSection1SlideComponent } from "./product-section1-slide/product-section1-slide.component";
import { ProductSection2OurPartnersComponent } from "./product-section2-our-partners/product-section2-our-partners.component";
import { ProductSection3CategoryElectronicsComponent } from "./product-section3-category-electronics/product-section3-category-electronics.component";

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [BreadcrumbNavigationComponent, ContainerComponent, RouterOutlet, ProductSection1SlideComponent, ProductSection2OurPartnersComponent, ProductSection3CategoryElectronicsComponent],
  templateUrl: './product-list.component.html',
  styleUrl: './product-list.component.scss'
})
export class ProductListComponent {

}
