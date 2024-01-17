const cloneSymbol = Symbol('clone');

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
    if (typeof cloneSymbol !== 'symbol') {
      throw new Error('You cannot call cloneCar directly');
    }
  }

  cloneCar() {
    return new this.constructor(cloneSymbol);
  }
}
