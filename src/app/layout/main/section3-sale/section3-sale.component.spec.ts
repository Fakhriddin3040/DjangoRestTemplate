import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Section2SaleComponent } from './section2-sale.component';

describe('Section2SaleComponent', () => {
  let component: Section2SaleComponent;
  let fixture: ComponentFixture<Section2SaleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Section2SaleComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Section2SaleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
