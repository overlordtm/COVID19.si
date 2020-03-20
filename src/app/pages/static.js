import Page from 'app/page'
import * as StaticTemplate from 'templates/pages/static.hbs'
import * as d1 from 'content/about.md'
import * as d2 from 'content/team.md'

const _ = d1

export default class StaticPage extends Page {

  constructor(title, content) {
    super(title)
    this.content = content
  }

  template() {
    return this.content.then(module => {
      let ctx = {
        content: module.default,
      }
      return StaticTemplate(ctx)
    });
  }

}