import { Component } from '@angular/core';
import { ContainerComponent } from '../../../shared/container/container.component';
import { CountdownTimerComponent } from "../../../shared/components/countdown-timer/countdown-timer.component";

@Component({
  selector: 'app-section3-sale',
  standalone: true,
  imports: [
    ContainerComponent,
    CountdownTimerComponent,
    
],
  templateUrl: './section3-sale.component.html',
  styleUrl: './section3-sale.component.scss'
})
export class Section3SaleComponent {

}
