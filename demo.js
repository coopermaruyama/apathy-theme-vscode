// @ts-nocheck
/**
 * Apathy Theme Demo File
 * This file showcases the various syntax highlighting features
 * TODO: Add more examples
 * FIXME: Fix any color issues
 * NOTE: This is just for demonstration
 */

// Import statements
import React, { useState, useEffect } from "react";
import { someFunction } from "./utils";

// Constants and variables

const THEME_NAME = "Apathy";
const VERSION = "1.0.0";

let isDarkMode = true;
var oldStyleVar = "deprecated";

// Class definition
class ThemeDemo {
  constructor(name) {
    this.name = name;
    this.colors = {
      background: "#0F0D1A",
      foreground: "#E6E2D1",
      accent: "#FF7A00",
    };
  }

  // Method with various syntax elements
  async getDemoData(param1, param2 = "default") {
    try {
      // String literals and template strings
      const message = `Hello ${this.name}!`;
      const singleQuoted = "Single quoted string";
      const doubleQuoted = "Double quoted string";

      // Numbers and booleans
      const numbers = [42, 3.14, 0xff, 0b1010];
      const flags = [true, false, null, undefined];

      // Regular expressions
      const regex = /^[a-zA-Z0-9]+$/gi;

      // Functions and arrow functions
      const processData = (data) => {
        return data.map((item) => item.toLowerCase());
      };

      // Control flow
      if (param1 && param2) {
        for (let i = 0; i < numbers.length; i++) {
          console.log(`Number ${i}: ${numbers[i]}`);
        }
      } else {
        throw new Error("Invalid parameters");
      }

      // Async operations
      const result = await fetch("/api/data");
      return await result.json();
    } catch (error) {
      console.error("Error:", error.message);
      return null;
    }
  }
}

// Function expressions
const createTheme = function (options = {}) {
  const defaultOptions = {
    name: "Default",
    type: "dark",
    ...options,
  };

  return new ThemeDemo(defaultOptions.name);
};

// Arrow functions with destructuring
const { name, type } = createTheme({ name: "Apathy", type: "dark" });

// Modern JavaScript features
const themeConfig = {
  ...defaultOptions,
  features: ["syntax-highlighting", "ui-theming", "git-integration"],
  isRecommended: true,
};

// Export statement
export { ThemeDemo, createTheme };
export default themeConfig;

Project.prototype.addItem = function (itemName) {
  for (item in cart["trick"]) {
    this.ageNum = opts / 13; // NOTE This is an arbitrary number for now.-
    Cart.create({
      melons: true, // HACK This will clear out your bank account.-
      count: 34 + 4347, // TODO validation on these options. -
      when: "Super duper color man!", // XXX Nice and colored memos. -
    });
  }
};
var utilityCreate = function (numBoxes, location) {
  var parts = namespace.split("."),
    name = parts.pop;
  // Apparently 'insert' blocks on server if called-
  if (/^\s (.*) [0-9a-z]+||>?a$/.test(parts["name"]))
    throw new Error("Oh noes!");
  // Make sure this works
  return !isTypeSet(chapter) ? setTypeYes : MyClass.create();
};

// ----------------------------------------------------------------------------
// @Component - create items factory
// ----------------------------------------------------------------------------
if ((themeName && window.shouldRun) || catalog === null) {
  // XXX Might want to namespace
  window["property"].apply(this, arguments);

  // pubsub
  if (Meteor.isServer) {
    Meteor.publish(null, function () {
      return NoGuessworkChapters._collection.find();
    });
    NoGuessworkChapters.allow({
      insert: function () {
        return true; // Allow insertions
      },
      update: function () {
        return true; // Allow updates
      },
      remove: function () {
        return true; // Allow removals
      },
    });
  }
}
