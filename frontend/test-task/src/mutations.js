import gql from 'graphql-tag'

export const USER_SIGNUP  = gql`
  mutation (
    $first_name: String!,
    $last_name: String!,
    $profile_region: JSONString!,
    $profile_city: JSONString!,
    $username: String!,
    $password: String!,
    $joined_date: String!,
    $percent_prepayment: String,
    $prepayment_fixed: String,
    $non_refundable_prepayment: String,
    $color_theme: Boolean!,
    $notifications_coming: Boolean!,
    $notifications_past: Boolean!,
    $cope_backup: Boolean!,
    $synchronization: Boolean!,
  ) {
    create_user(
      first_name: $first_name,
      last_name: $last_name,
      profile_region: $profile_region,
      profile_city: $profile_city,
      username: $username,
      password: $password,
      joined_date: $joined_date,
      percent_prepayment: $percent_prepayment,
      prepayment_fixed: $prepayment_fixed,
      non_refundable_prepayment: $non_refundable_prepayment,
      color_theme: $color_theme,
      notifications_coming: $notifications_coming,
      notifications_past: $notifications_past,
      cope_backup: $cope_backup,
      synchronization: $synchronization,
    ) {
      success_cruser
    }
  }
`
