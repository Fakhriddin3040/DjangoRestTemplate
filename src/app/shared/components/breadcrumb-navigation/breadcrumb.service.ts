import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BreadcrumbService {
  private breadcrumbs = new BehaviorSubject<string[]>(['home']);
  breadcrumbs$ = this.breadcrumbs.asObservable();

  updateBreadcrumbs(newCrumb: string) {
    const currentCrumbs = this.breadcrumbs.getValue();
    this.breadcrumbs.next([...currentCrumbs, newCrumb]);
  }
}
