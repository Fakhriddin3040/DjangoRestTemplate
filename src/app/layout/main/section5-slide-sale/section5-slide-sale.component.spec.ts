import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Section5SlideSaleComponent } from './section5-slide-sale.component';

describe('Section5SlideSaleComponent', () => {
  let component: Section5SlideSaleComponent;
  let fixture: ComponentFixture<Section5SlideSaleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Section5SlideSaleComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Section5SlideSaleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
