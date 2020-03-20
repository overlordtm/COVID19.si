import * as showdown from 'showdown'
import * as aboutContent from '../content/about.md'

export function render() {
  let opts = {
    // simplifiedAutoLink: true,
    // tables: true,
  }

  let converter = new showdown.Converter(opts)
  converter.setFlavor('github')
    return converter.makeHtml(aboutContent)
}