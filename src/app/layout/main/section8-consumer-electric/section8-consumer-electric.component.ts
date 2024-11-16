import { Component, OnInit, AfterViewInit, Renderer2, Inject, PLATFORM_ID } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import { ContainerComponent } from '../../../shared/container/container.component';
import { ButtonShopNowComponent } from '../../../shared/components/buttons/button-shop-now/button-shop-now.component';

@Component({
  selector: 'app-section8-consumer-electric',
  standalone: true,
  imports: [ContainerComponent, ButtonShopNowComponent],
  templateUrl: './section8-consumer-electric.component.html',
  styleUrl: './section8-consumer-electric.component.scss'
})
export class Section8ConsumerElectricComponent implements OnInit, AfterViewInit {
  private scriptLoaded = false;

  constructor(
    private renderer: Renderer2,
    @Inject(PLATFORM_ID) private platformId: Object
  ) {}

  ngOnInit(): void {
    if (isPlatformBrowser(this.platformId)) {
      // Загружаем скрипт и стили для Swiper, если они еще не загружены
      const script = this.renderer.createElement('script');
      script.src = 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-element-bundle.min.js';
      script.onload = () => {
        this.scriptLoaded = true;
        this.initializeSwiper();
      };
      script.onerror = (error: any) => {
        console.error('Ошибка загрузки скрипта Swiper:', error);
      };
      this.renderer.appendChild(document.body, script);

      const link = this.renderer.createElement('link');
      link.rel = 'stylesheet';
      link.href = 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-element-bundle.min.css';
      this.renderer.appendChild(document.head, link);
    }
  }

  ngAfterViewInit(): void {
    if (this.scriptLoaded) {
      this.initializeSwiper();
    }

    if (isPlatformBrowser(this.platformId)) {
      const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
      tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new (window as any).bootstrap.Tooltip(tooltipTriggerEl);
      });
    }
  }

  private initializeSwiper(): void {
    if (window['Swiper']) {
      const Swiper = window['Swiper'];
      var swiper = new Swiper(".section6Swiper", {
        slidesPerView: 3,
        grid: {
          rows: 2,
        },
        
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
      });
    } else {
      console.error('Swiper не найден.');
    }
  }
}