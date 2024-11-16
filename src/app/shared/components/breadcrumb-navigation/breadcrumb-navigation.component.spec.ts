import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BreadcrumbNavigationComponent } from './breadcrumb-navigation.component';

describe('BreadcrumbNavigationComponent', () => {
  let component: BreadcrumbNavigationComponent;
  let fixture: ComponentFixture<BreadcrumbNavigationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BreadcrumbNavigationComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BreadcrumbNavigationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
