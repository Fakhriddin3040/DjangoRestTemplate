import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FooterSection4PaymentComponent } from './footer-section4-payment.component';

describe('FooterSection4PaymentComponent', () => {
  let component: FooterSection4PaymentComponent;
  let fixture: ComponentFixture<FooterSection4PaymentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FooterSection4PaymentComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FooterSection4PaymentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
