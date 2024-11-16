"use strict";
var __esDecorate = (this && this.__esDecorate) || function (ctor, descriptorIn, decorators, contextIn, initializers, extraInitializers) {
    function accept(f) { if (f !== void 0 && typeof f !== "function") throw new TypeError("Function expected"); return f; }
    var kind = contextIn.kind, key = kind === "getter" ? "get" : kind === "setter" ? "set" : "value";
    var target = !descriptorIn && ctor ? contextIn["static"] ? ctor : ctor.prototype : null;
    var descriptor = descriptorIn || (target ? Object.getOwnPropertyDescriptor(target, contextIn.name) : {});
    var _, done = false;
    for (var i = decorators.length - 1; i >= 0; i--) {
        var context = {};
        for (var p in contextIn) context[p] = p === "access" ? {} : contextIn[p];
        for (var p in contextIn.access) context.access[p] = contextIn.access[p];
        context.addInitializer = function (f) { if (done) throw new TypeError("Cannot add initializers after decoration has completed"); extraInitializers.push(accept(f || null)); };
        var result = (0, decorators[i])(kind === "accessor" ? { get: descriptor.get, set: descriptor.set } : descriptor[key], context);
        if (kind === "accessor") {
            if (result === void 0) continue;
            if (result === null || typeof result !== "object") throw new TypeError("Object expected");
            if (_ = accept(result.get)) descriptor.get = _;
            if (_ = accept(result.set)) descriptor.set = _;
            if (_ = accept(result.init)) initializers.unshift(_);
        }
        else if (_ = accept(result)) {
            if (kind === "field") initializers.unshift(_);
            else descriptor[key] = _;
        }
    }
    if (target) Object.defineProperty(target, contextIn.name, descriptor);
    done = true;
};
var __runInitializers = (this && this.__runInitializers) || function (thisArg, initializers, value) {
    var useValue = arguments.length > 2;
    for (var i = 0; i < initializers.length; i++) {
        value = useValue ? initializers[i].call(thisArg, value) : initializers[i].call(thisArg);
    }
    return useValue ? value : void 0;
};
var __setFunctionName = (this && this.__setFunctionName) || function (f, name, prefix) {
    if (typeof name === "symbol") name = name.description ? "[".concat(name.description, "]") : "";
    return Object.defineProperty(f, "name", { configurable: true, value: prefix ? "".concat(prefix, " ", name) : name });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.RegisterComponent = void 0;
var core_1 = require("@angular/core");
var input_1 = require("@angular/material/input");
var form_field_1 = require("@angular/material/form-field");
var forms_1 = require("@angular/forms");
var router_1 = require("@angular/router"); // Импортируем Router из Angular
var common_1 = require("@angular/common");
var RegisterComponent = function () {
    var _classDecorators = [(0, core_1.Component)({
            selector: 'app-register',
            standalone: true,
            imports: [forms_1.FormsModule, form_field_1.MatFormFieldModule, input_1.MatInputModule],
            templateUrl: './register.component.html',
            styleUrl: './register.component.scss'
        })];
    var _classDescriptor;
    var _classExtraInitializers = [];
    var _classThis;
    var RegisterComponent = _classThis = /** @class */ (function () {
        function RegisterComponent_1() {
            // Используем новую функцию inject для инъекции зависимостей
            this.platformId = (0, core_1.inject)(core_1.PLATFORM_ID);
            this.router = (0, core_1.inject)(router_1.Router); // Используем Angular Router
        }
        RegisterComponent_1.prototype.ngOnInit = function () {
            var _this = this;
            // Проверяем, работает ли приложение в браузере
            if ((0, common_1.isPlatformBrowser)(this.platformId)) {
                this.loadGoogleScript().then(function () {
                    google.accounts.id.initialize({
                        client_id: '409809896736-fckja2ujg9itegt7r06k2itrt409472a.apps.googleusercontent.com',
                        callback: function (response) {
                            _this.handlelogin(response);
                            return false; // Останавливаем обработку дальнейших событий
                        },
                    });
                    google.accounts.id.renderButton(document.getElementById('googleSignInButton'), { theme: 'outline', size: 'large' });
                });
            }
        };
        RegisterComponent_1.prototype.loadGoogleScript = function () {
            return new Promise(function (resolve, reject) {
                if (typeof google !== 'undefined') {
                    resolve();
                }
                else {
                    var script = document.createElement('script');
                    script.src = 'https://accounts.google.com/gsi/client';
                    script.async = true;
                    script.defer = true;
                    script.onload = function () { return resolve(); };
                    script.onerror = function (error) {
                        console.error('Error loading Google script:', error);
                        reject(error);
                    };
                    document.body.appendChild(script);
                }
            });
        };
        RegisterComponent_1.prototype.decoderToken = function (token) {
            return JSON.parse(atob(token.split('.')[1]));
        };
        RegisterComponent_1.prototype.handlelogin = function (response) {
            if (response) {
                try {
                    console.log('Google login response:', response);
                    var payload = this.decoderToken(response.credential);
                    if ((0, common_1.isPlatformBrowser)(this.platformId)) {
                        sessionStorage.setItem('loggedInUser', JSON.stringify({
                            name: payload.name,
                            email: payload.email,
                            picture: payload.picture,
                        }));
                    }
                }
                catch (error) {
                    console.error('Error handling login response:', error);
                }
            }
        };
        return RegisterComponent_1;
    }());
    __setFunctionName(_classThis, "RegisterComponent");
    (function () {
        var _metadata = typeof Symbol === "function" && Symbol.metadata ? Object.create(null) : void 0;
        __esDecorate(null, _classDescriptor = { value: _classThis }, _classDecorators, { kind: "class", name: _classThis.name, metadata: _metadata }, null, _classExtraInitializers);
        RegisterComponent = _classThis = _classDescriptor.value;
        if (_metadata) Object.defineProperty(_classThis, Symbol.metadata, { enumerable: true, configurable: true, writable: true, value: _metadata });
        __runInitializers(_classThis, _classExtraInitializers);
    })();
    return RegisterComponent = _classThis;
}();
exports.RegisterComponent = RegisterComponent;
