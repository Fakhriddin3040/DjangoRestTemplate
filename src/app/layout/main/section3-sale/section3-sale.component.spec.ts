import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Section3SaleComponent } from './section3-sale.component';

describe('Section3SaleComponent', () => {
  let component: Section3SaleComponent;
  let fixture: ComponentFixture<Section3SaleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Section3SaleComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Section3SaleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
