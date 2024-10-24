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
exports.HeaderSection4MenuComponent = void 0;
var core_1 = require("@angular/core");
var container_component_1 = require("../../../shared/container/container.component");
var app_menu_component_1 = require("../../../shared/components/menu/app-menu/app-menu.component");
var menu_home_layout_component_1 = require("../../../shared/components/menu/menu-home-layout/menu-home-layout.component");
var menu_category_component_1 = require("../../../shared/components/menu/menu-category/menu-category.component");
var menu_product_component_1 = require("../../../shared/components/menu/menu-product/menu-product.component");
var menu_blog_component_1 = require("../../../shared/components/menu/menu-blog/menu-blog.component");
var button_1 = require("@angular/material/button");
var HeaderSection4MenuComponent = function () {
    var _classDecorators = [(0, core_1.Component)({
            selector: 'app-header-section4-menu',
            standalone: true,
            imports: [
                container_component_1.ContainerComponent,
                app_menu_component_1.AppMenuComponent,
                menu_home_layout_component_1.MenuHomeLayoutComponent,
                menu_category_component_1.MenuCategoryComponent,
                menu_product_component_1.MenuProductComponent,
                menu_blog_component_1.MenuBlogComponent,
                button_1.MatButtonModule
            ],
            templateUrl: './header-section4-menu.component.html',
            styleUrl: './header-section4-menu.component.scss',
        })];
    var _classDescriptor;
    var _classExtraInitializers = [];
    var _classThis;
    var HeaderSection4MenuComponent = _classThis = /** @class */ (function () {
        function HeaderSection4MenuComponent_1() {
        }
        return HeaderSection4MenuComponent_1;
    }());
    __setFunctionName(_classThis, "HeaderSection4MenuComponent");
    (function () {
        var _metadata = typeof Symbol === "function" && Symbol.metadata ? Object.create(null) : void 0;
        __esDecorate(null, _classDescriptor = { value: _classThis }, _classDecorators, { kind: "class", name: _classThis.name, metadata: _metadata }, null, _classExtraInitializers);
        HeaderSection4MenuComponent = _classThis = _classDescriptor.value;
        if (_metadata) Object.defineProperty(_classThis, Symbol.metadata, { enumerable: true, configurable: true, writable: true, value: _metadata });
        __runInitializers(_classThis, _classExtraInitializers);
    })();
    return HeaderSection4MenuComponent = _classThis;
}();
exports.HeaderSection4MenuComponent = HeaderSection4MenuComponent;
