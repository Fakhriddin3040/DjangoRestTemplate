import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FooterSection1SubscribeComponent } from './footer-section1-subscribe.component';

describe('FooterSection1SubscribeComponent', () => {
  let component: FooterSection1SubscribeComponent;
  let fixture: ComponentFixture<FooterSection1SubscribeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FooterSection1SubscribeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FooterSection1SubscribeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
