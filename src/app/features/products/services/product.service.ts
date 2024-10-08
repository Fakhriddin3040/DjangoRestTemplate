import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ProductService {

  private apiUrl = 'http://localhost:3000/items';  // Ваш URL для API

  constructor(private http: HttpClient) {}

  // Метод для получения данных
  fetchData(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}
