import { Component } from '@angular/core';
import { ContainerComponent } from '../../shared/container/container.component';
import { FooterSection1SubscribeComponent } from './footer-section1-subscribe/footer-section1-subscribe.component';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [ContainerComponent, FooterSection1SubscribeComponent],
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.scss'
})
export class FooterComponent {
  
}
