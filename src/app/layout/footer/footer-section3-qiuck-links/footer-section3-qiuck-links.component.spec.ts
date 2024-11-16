import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FooterSection3QiuckLinksComponent } from './footer-section3-qiuck-links.component';

describe('FooterSection3QiuckLinksComponent', () => {
  let component: FooterSection3QiuckLinksComponent;
  let fixture: ComponentFixture<FooterSection3QiuckLinksComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FooterSection3QiuckLinksComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FooterSection3QiuckLinksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
