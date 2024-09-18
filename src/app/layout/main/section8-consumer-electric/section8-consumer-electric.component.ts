import { Component } from '@angular/core';
import { ContainerComponent } from '../../../shared/container/container.component';
import { ButtonShopNowComponent } from '../../../shared/components/buttons/button-shop-now/button-shop-now.component';

@Component({
  selector: 'app-section8-consumer-electric',
  standalone: true,
  imports: [ContainerComponent, ButtonShopNowComponent],
  templateUrl: './section8-consumer-electric.component.html',
  styleUrl: './section8-consumer-electric.component.scss'
})
export class Section8ConsumerElectricComponent {

}
