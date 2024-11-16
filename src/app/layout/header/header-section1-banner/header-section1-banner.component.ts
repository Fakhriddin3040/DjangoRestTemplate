import { Component } from '@angular/core';
import { ContainerComponent } from '../../../shared/container/container.component';

@Component({
  selector: 'app-header-section1-banner',
  standalone: true,
  imports: [ContainerComponent],
  templateUrl: './header-section1-banner.component.html',
  styleUrl: './header-section1-banner.component.scss'
})
export class Section1BannerComponent {
  imageUrl = 'assets/images/promo/promo1.png';
  imageUrl2 = 'assets/images/promo/promo2.png';
}