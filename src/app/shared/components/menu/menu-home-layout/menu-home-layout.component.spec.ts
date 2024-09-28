import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MenuHomeLayoutComponent } from './menu-home-layout.component';

describe('MenuHomeLayoutComponent', () => {
  let component: MenuHomeLayoutComponent;
  let fixture: ComponentFixture<MenuHomeLayoutComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MenuHomeLayoutComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MenuHomeLayoutComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
