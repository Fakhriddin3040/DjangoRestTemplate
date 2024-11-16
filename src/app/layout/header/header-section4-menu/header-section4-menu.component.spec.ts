import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeaderSection4MenuComponent } from './header-section4-menu.component';

describe('HeaderSection4MenuComponent', () => {
  let component: HeaderSection4MenuComponent;
  let fixture: ComponentFixture<HeaderSection4MenuComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HeaderSection4MenuComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HeaderSection4MenuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
