import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Section4ShowReverseTimeSaleComponent } from './section4-show-reverse-time-sale.component';

describe('Section4ShowReverseTimeSaleComponent', () => {
  let component: Section4ShowReverseTimeSaleComponent;
  let fixture: ComponentFixture<Section4ShowReverseTimeSaleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Section4ShowReverseTimeSaleComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Section4ShowReverseTimeSaleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
