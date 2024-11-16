"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.authGuard = void 0;
var router_1 = require("@angular/router");
var core_1 = require("@angular/core");
// Создание функции authGuard с проверкой авторизации
var authGuard = function (route, state) {
    var router = (0, core_1.inject)(router_1.Router); // Используем DI для получения Router
    // Получаем данные о текущем пользователе из sessionStorage
    var user = sessionStorage.getItem('loggedInUser');
    // Если пользователь не найден, перенаправляем на страницу входа
    if (!user) {
        router.navigate(['/login']); // Путь к вашей странице входа
        return false; // Запретить доступ к защищенному маршруту
    }
    return true; // Разрешить доступ к защищенному маршруту
};
exports.authGuard = authGuard;
