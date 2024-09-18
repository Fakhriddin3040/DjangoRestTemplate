import { Component } from '@angular/core';
import { ContainerComponent } from '../../../shared/container/container.component';
import { ButtonShopNowComponent } from '../../../shared/components/buttons/button-shop-now/button-shop-now.component';

@Component({
  selector: 'app-section9-home-garden-kitchen',
  standalone: true,
  imports: [ContainerComponent, ButtonShopNowComponent],
  templateUrl: './section9-home-garden-kitchen.component.html',
  styleUrl: './section9-home-garden-kitchen.component.scss'
})
export class Section9HomeGardenKitchenComponent {
  
}
