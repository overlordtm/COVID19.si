import * as showdown from 'showdown'
import Page from 'app/page'
import * as StaticTemplate from 'templates/pages/static.hbs'

export default class StaticPage extends Page {

  constructor(title, url) {
    super(title)
    this.url = url
  }

  template() {
    let opts = {
      simpleLineBreaks: false,
      simplifiedAutoLink: true,
    }
    let converter = new showdown.Converter(opts)
    converter.setFlavor('github')

    return fetch(this.url).then(response => {
      return response.text().then(data => {
        console.log("data", data)
        let ctx = {
          content: converter.makeHtml(data),
        }
        return StaticTemplate(ctx)
      })
    })
  }

}