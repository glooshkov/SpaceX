import gql from 'graphql-tag'

export const SITE_INFO = gql`
  query {
    site {
      name
    }
  }
`

export const All_BENEFITS = gql`
  query {
    all_benefits {
      top_text
      integer
      bot_text
    }
  }
`

export const All_MENU = gql`
  query {
    all_menu {
      text
    }
  }
`