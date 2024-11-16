import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FooterSection2ContactComponent } from './footer-section2-contact.component';

describe('FooterSection2ContactComponent', () => {
  let component: FooterSection2ContactComponent;
  let fixture: ComponentFixture<FooterSection2ContactComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FooterSection2ContactComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FooterSection2ContactComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
