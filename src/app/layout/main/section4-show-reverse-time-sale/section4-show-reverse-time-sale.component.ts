import { Component } from '@angular/core';
import { CountdownTimerComponent } from "../../../shared/components/countdown-timer/countdown-timer.component";
import { ContainerComponent } from '../../../shared/container/container.component';


@Component({
  selector: 'app-section4-show-reverse-time-sale',
  standalone: true,
  imports: [
    CountdownTimerComponent,
    ContainerComponent
  ],
  templateUrl: './section4-show-reverse-time-sale.component.html',
  styleUrl: './section4-show-reverse-time-sale.component.scss'
})
export class Section4ShowReverseTimeSaleComponent {

}
