import * as bun from 'bun'


const colors = {
  purple: '#8564d8c7',
}
const contents = {
    name: "Apathy (Experimental)",
    type: "dark",
    colors: {
      "editor.background": "#0A0A0A",
      "editor.foreground": "#E0E0E0",
      "editorLineNumber.foreground": "#5A5A5A",
      "editorLineNumber.activeForeground": "#FFFFFF",
      "editorCursor.foreground": "#FFFFFF",
      "editor.selectionBackground": "#333333",
      "editor.selectionHighlightBackground": "#222222",
      "editor.wordHighlightBackground": "#222222",
      "editor.wordHighlightStrongBackground": "#222222"
    },
    tokenColors: [
      {
        scope: [
          "comment",
          "punctuation.definition.comment",
          "string.comment"
        ],
        settings: {
          foreground: "#5A5A5A",
          fontStyle: "italic"
        }
      },
    ]
  }

async function main() {
  await bun.write('./themes/default.yaml', JSON.stringify(contents, null, 2))
}

main()
  .then(() => console.log('Wrote default theme'))
  .catch((err) => console.error(err))