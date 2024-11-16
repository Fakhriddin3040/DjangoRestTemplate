import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Section1BannerComponent } from './header-section1-banner.component';

describe('Section1BannerComponent', () => {
  let component: Section1BannerComponent;
  let fixture: ComponentFixture<Section1BannerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Section1BannerComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Section1BannerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
