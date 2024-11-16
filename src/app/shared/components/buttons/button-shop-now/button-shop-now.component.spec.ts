import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ButtonShopNowComponent } from './button-shop-now.component';

describe('ButtonShopNowComponent', () => {
  let component: ButtonShopNowComponent;
  let fixture: ComponentFixture<ButtonShopNowComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ButtonShopNowComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ButtonShopNowComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
