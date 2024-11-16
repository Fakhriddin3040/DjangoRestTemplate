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
exports.CountdownTimerComponent = void 0;
var core_1 = require("@angular/core");
var CountdownTimerComponent = function () {
    var _classDecorators = [(0, core_1.Component)({
            selector: 'app-countdown-timer',
            standalone: true,
            templateUrl: './countdown-timer.component.html',
            styleUrls: ['./countdown-timer.component.scss'],
        })];
    var _classDescriptor;
    var _classExtraInitializers = [];
    var _classThis;
    var _day_decorators;
    var _day_initializers = [];
    var _day_extraInitializers = [];
    var _hour_decorators;
    var _hour_initializers = [];
    var _hour_extraInitializers = [];
    var _minute_decorators;
    var _minute_initializers = [];
    var _minute_extraInitializers = [];
    var _second_decorators;
    var _second_initializers = [];
    var _second_extraInitializers = [];
    var CountdownTimerComponent = _classThis = /** @class */ (function () {
        function CountdownTimerComponent_1() {
            this.day = __runInitializers(this, _day_initializers, void 0);
            this.hour = (__runInitializers(this, _day_extraInitializers), __runInitializers(this, _hour_initializers, void 0));
            this.minute = (__runInitializers(this, _hour_extraInitializers), __runInitializers(this, _minute_initializers, void 0));
            this.second = (__runInitializers(this, _minute_extraInitializers), __runInitializers(this, _second_initializers, void 0));
            __runInitializers(this, _second_extraInitializers);
        }
        CountdownTimerComponent_1.prototype.ngAfterViewInit = function () {
            var _this = this;
            if (typeof window !== 'undefined') {
                this.updateCountdown();
                setInterval(function () { return _this.updateCountdown(); }, 1000);
            }
        };
        CountdownTimerComponent_1.prototype.updateCountdown = function () {
            var currentYear = new Date().getFullYear();
            var nextYear = new Date("January 01 ".concat(currentYear + 1, " 00:00:00"));
            var currentTime = new Date();
            var diff = nextYear.getTime() - currentTime.getTime();
            var dayLeft = Math.floor(diff / 1000 / 60 / 60 / 24);
            var hourLeft = Math.floor(diff / 1000 / 60 / 60) % 24;
            var minutesLeft = Math.floor(diff / 1000 / 60) % 60;
            var secondLeft = Math.floor(diff / 1000) % 60;
            // Обновляем значения через ElementRef
            this.day.nativeElement.textContent = dayLeft.toString().padStart(2, '0');
            this.hour.nativeElement.textContent = hourLeft.toString().padStart(2, '0');
            this.minute.nativeElement.textContent = minutesLeft.toString().padStart(2, '0');
            this.second.nativeElement.textContent = secondLeft.toString().padStart(2, '0');
        };
        return CountdownTimerComponent_1;
    }());
    __setFunctionName(_classThis, "CountdownTimerComponent");
    (function () {
        var _metadata = typeof Symbol === "function" && Symbol.metadata ? Object.create(null) : void 0;
        _day_decorators = [(0, core_1.ViewChild)('day', { static: false })];
        _hour_decorators = [(0, core_1.ViewChild)('hour', { static: false })];
        _minute_decorators = [(0, core_1.ViewChild)('minute', { static: false })];
        _second_decorators = [(0, core_1.ViewChild)('second', { static: false })];
        __esDecorate(null, null, _day_decorators, { kind: "field", name: "day", static: false, private: false, access: { has: function (obj) { return "day" in obj; }, get: function (obj) { return obj.day; }, set: function (obj, value) { obj.day = value; } }, metadata: _metadata }, _day_initializers, _day_extraInitializers);
        __esDecorate(null, null, _hour_decorators, { kind: "field", name: "hour", static: false, private: false, access: { has: function (obj) { return "hour" in obj; }, get: function (obj) { return obj.hour; }, set: function (obj, value) { obj.hour = value; } }, metadata: _metadata }, _hour_initializers, _hour_extraInitializers);
        __esDecorate(null, null, _minute_decorators, { kind: "field", name: "minute", static: false, private: false, access: { has: function (obj) { return "minute" in obj; }, get: function (obj) { return obj.minute; }, set: function (obj, value) { obj.minute = value; } }, metadata: _metadata }, _minute_initializers, _minute_extraInitializers);
        __esDecorate(null, null, _second_decorators, { kind: "field", name: "second", static: false, private: false, access: { has: function (obj) { return "second" in obj; }, get: function (obj) { return obj.second; }, set: function (obj, value) { obj.second = value; } }, metadata: _metadata }, _second_initializers, _second_extraInitializers);
        __esDecorate(null, _classDescriptor = { value: _classThis }, _classDecorators, { kind: "class", name: _classThis.name, metadata: _metadata }, null, _classExtraInitializers);
        CountdownTimerComponent = _classThis = _classDescriptor.value;
        if (_metadata) Object.defineProperty(_classThis, Symbol.metadata, { enumerable: true, configurable: true, writable: true, value: _metadata });
        __runInitializers(_classThis, _classExtraInitializers);
    })();
    return CountdownTimerComponent = _classThis;
}();
exports.CountdownTimerComponent = CountdownTimerComponent;
