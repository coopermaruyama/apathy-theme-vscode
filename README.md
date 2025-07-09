# Apathy Theme for VS Code

A sophisticated dark color theme ported from the original Atom version, featuring deep purple/black backgrounds with vibrant, neon-like syntax highlighting. Apathy provides excellent contrast and readability while maintaining a visually striking aesthetic.

## 📸 Screenshots

![screenshot](./assets/Screenshot%202025-07-09%20at%201.21.00 PM.png)
![screenshot](./assets/Screenshot%202025-07-09%20at%2012.08.22 PM.png)
![screenshot](./assets/Screenshot%202025-07-09%20at%201.21.58 PM.png)
![screenshot](./assets/Screenshot%202025-07-09%20at%201.21.14 PM.png)

## ✨ Features

- **Deep Dark Background**: Rich purple-black background (`#0F0D1A`) that's easy on the eyes
- **Vibrant Syntax Highlighting**: Carefully chosen colors that provide excellent contrast
- **Language-Specific Optimizations**: Enhanced highlighting for JavaScript, TypeScript, Python, CSS, JSON, and more
- **Comprehensive UI Theming**: Full VS Code interface theming including sidebars, panels, and status bar
- **Git Integration**: Clear colors for git decorations and diff highlighting
- **Accessibility**: High contrast ratios for better readability

## 🎨 Color Palette

Here are some key colors from the Apathy theme palette:

| Name          |                                                            Sample                                                            |    Hex    |
| ------------- | :--------------------------------------------------------------------------------------------------------------------------: | :-------: |
| Background    | <span style="display:inline-block;width:24px;height:24px;background:#0F0D1A;border-radius:4px;border:1px solid #333"></span> | `#0F0D1A` |
| Foreground    | <span style="display:inline-block;width:24px;height:24px;background:#E6E6F1;border-radius:4px;border:1px solid #333"></span> | `#E6E6F1` |
| Accent Purple | <span style="display:inline-block;width:24px;height:24px;background:#A277FF;border-radius:4px;border:1px solid #333"></span> | `#A277FF` |
| Neon Blue     | <span style="display:inline-block;width:24px;height:24px;background:#61FFCA;border-radius:4px;border:1px solid #333"></span> | `#61FFCA` |
| Soft Yellow   | <span style="display:inline-block;width:24px;height:24px;background:#FFCA85;border-radius:4px;border:1px solid #333"></span> | `#FFCA85` |
| Vibrant Pink  | <span style="display:inline-block;width:24px;height:24px;background:#FF6767;border-radius:4px;border:1px solid #333"></span> | `#FF6767` |
| Muted Cyan    | <span style="display:inline-block;width:24px;height:24px;background:#21BFC2;border-radius:4px;border:1px solid #333"></span> | `#21BFC2` |
| Soft Gray     | <span style="display:inline-block;width:24px;height:24px;background:#6D6D7C;border-radius:4px;border:1px solid #333"></span> | `#6D6D7C` |

> _Colors shown above are representative samples from the theme's JSON file._

## 🚀 Installation

### From VS Code Marketplace

1. Open VS Code
2. Go to Extensions (`Ctrl+Shift+X` / `Cmd+Shift+X`)
3. Search for "Apathy Theme"
4. Click Install
5. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
6. Type "Color Theme" and select "Preferences: Color Theme"
7. Choose "Apathy" from the list

### From Source

1. Clone this repository
2. Copy the folder to your VS Code extensions directory:
   - **Windows**: `%USERPROFILE%\.vscode\extensions`
   - **macOS**: `~/.vscode/extensions`
   - **Linux**: `~/.vscode/extensions`
3. Restart VS Code
4. Select the theme as described above

## 🛠 Supported Languages

Apathy theme includes optimized highlighting for:

- JavaScript/TypeScript
- Python
- CSS/SCSS/Less
- HTML
- JSON
- Markdown
- Git
- And many more...

## 🎯 Design Philosophy

Apathy was designed with these principles in mind:

1. **Readability First**: Every color choice prioritizes code readability
2. **Semantic Highlighting**: Similar language constructs use consistent colors
3. **Visual Hierarchy**: Important elements stand out while maintaining harmony
4. **Eye Comfort**: Dark background reduces eye strain during long coding sessions
5. **Aesthetic Appeal**: Beautiful colors that make coding enjoyable

## 🔧 Customization

If you want to customize the theme, you can:

1. Open VS Code settings (`Ctrl+,` / `Cmd+,`)
2. Search for "workbench.colorCustomizations"
3. Add your custom colors:

```json
{
  "workbench.colorCustomizations": {
    "[Apathy]": {
      "editor.background": "#your-color-here"
    }
  }
}
```

## 🐛 Issues & Feedback

Found a bug or have a suggestion? Please open an issue on [GitHub](https://github.com/coopermaruyama/apathy-theme/issues).

## 📝 License

This theme is licensed under the [MIT License](LICENSE).

## 🙏 Credits

Originally created for Atom by Cooper Maruyama. Ported to VS Code with love and attention to detail.

## 🌟 Show Your Support

If you enjoy using Apathy, consider:

- ⭐ Starring the project on GitHub
- 📝 Leaving a review on the VS Code Marketplace
- 🐛 Reporting issues or suggesting improvements
- 📢 Sharing with other developers

---

_Happy coding with Apathy! 💜_
