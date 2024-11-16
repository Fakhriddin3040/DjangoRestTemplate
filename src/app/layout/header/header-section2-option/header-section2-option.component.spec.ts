import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeaderSection1OptionComponent } from './header-section2-option.component';

describe('HeaderSection1OptionComponent', () => {
  let component: HeaderSection1OptionComponent;
  let fixture: ComponentFixture<HeaderSection1OptionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HeaderSection1OptionComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HeaderSection1OptionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
