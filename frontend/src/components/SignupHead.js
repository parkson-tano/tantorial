import React from 'react'
import { Title, Text, Anchor } from '@mantine/core'
import { Link } from 'react-router-dom'

function SignupHead({title}) {
  return (
    <div>
          <Title
              align="center"
              sx={(theme) => ({
                  fontFamily: `Greycliff CF, ${theme.fontFamily}`,
                  fontWeight: 900,
              })}
          >
              {title} {" "} Registration
          </Title>
          <Text color="dimmed" size="sm" align="center" mt={5}>
              Already have an account?{" "}
              <Link to="/login">
                  Login
              </Link>
          </Text>
    </div>
  )
}

export default SignupHead