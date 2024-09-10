import { Component, AfterViewInit, ElementRef, ViewChild } from '@angular/core';

@Component({
  selector: 'app-countdown-timer',
  standalone: true,
  templateUrl: './countdown-timer.component.html',
  styleUrls: ['./countdown-timer.component.scss'],
})
export class CountdownTimerComponent implements AfterViewInit  {
 
  @ViewChild('day', { static: false }) day!: ElementRef;
  @ViewChild('hour', { static: false }) hour!: ElementRef;
  @ViewChild('minute', { static: false }) minute!: ElementRef;
  @ViewChild('second', { static: false }) second!: ElementRef;

  ngAfterViewInit(): void {
    if (typeof window !== 'undefined') {
      this.updateCountdown();
      setInterval(() => this.updateCountdown(), 1000);
    }
  }

  updateCountdown() {
    const currentYear = new Date().getFullYear();
    const nextYear = new Date(`January 01 ${currentYear + 1} 00:00:00`);
    const currentTime = new Date();
    const diff = nextYear.getTime() - currentTime.getTime();

    const dayLeft = Math.floor(diff / 1000 / 60 / 60 / 24);
    const hourLeft = Math.floor(diff / 1000 / 60 / 60) % 24;
    const minutesLeft = Math.floor(diff / 1000 / 60) % 60;
    const secondLeft = Math.floor(diff / 1000) % 60;

    // Обновляем значения через ElementRef
    this.day.nativeElement.textContent = dayLeft.toString().padStart(2, '0');
    this.hour.nativeElement.textContent = hourLeft.toString().padStart(2, '0');
    this.minute.nativeElement.textContent = minutesLeft.toString().padStart(2, '0');
    this.second.nativeElement.textContent = secondLeft.toString().padStart(2, '0');
  }
}
