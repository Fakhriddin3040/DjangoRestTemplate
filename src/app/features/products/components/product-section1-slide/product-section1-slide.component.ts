import { Component, OnInit, AfterViewInit, Renderer2, Inject, PLATFORM_ID  } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';


@Component({
  selector: 'app-product-section1-slide',
  standalone: true,
  imports: [],
  templateUrl: './product-section1-slide.component.html',
  styleUrl: './product-section1-slide.component.scss'
})
export class ProductSection1SlideComponent implements OnInit, AfterViewInit  {
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
      var swiper = new Swiper(".mySwiper", {
        speed: 600,
        parallax: true,
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      });
    } else {
      console.error('Swiper не найден.');
    }
  }
}
