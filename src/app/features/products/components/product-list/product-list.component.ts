import { Component } from '@angular/core';
import { BreadcrumbNavigationComponent } from "../../../../shared/components/breadcrumb-navigation/breadcrumb-navigation.component";
import { ContainerComponent } from "../../../../shared/container/container.component";
import { Routes } from '@angular/router';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [BreadcrumbNavigationComponent, ContainerComponent],
  templateUrl: './product-list.component.html',
  styleUrl: './product-list.component.scss'
})
export class ProductListComponent {

}
