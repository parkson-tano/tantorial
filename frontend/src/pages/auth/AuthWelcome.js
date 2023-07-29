import React from 'react'
import { Card, Container, SimpleGrid, Text } from '@mantine/core'
import WelcomeCard from '../../components/WelcomeCard'
function AuthWelcome() {
  return (
    <div
    style={{
      backgroundImage: `url(https://app.gradely.co/auth/img/AuthBg.0d514f33.svg)`,
    }}
    >
  <Container
      style={{
        display: 'block',
        marginTop: '5%',
        marginBottom: '5%',
      }}
    >
      <Text align="center" weight={700} size="xl">Welcome to Tantorial</Text>
      <Text align="center" weight={700} size="lg">Join Tantorial as </Text>
      <SimpleGrid cols={2} spacing="xl" verticalSpacing="xl" p="xl"
        breakpoints={[
          { maxWidth: 'md', cols: 2, spacing: 'md' },
          { maxWidth: 'sm', cols: 1, spacing: 'sm' },
          { maxWidth: 'xs', cols: 1, spacing: 'sm' },
        ]}
      >
        <WelcomeCard title="Student" description="For Students and Learners" url="/student-register" />
        <WelcomeCard title="Teacher" description="For Teachers and  tutors" url="/teacher-register" />
        <WelcomeCard title="School" description="For school adminstration" url="/school-register" />
        <WelcomeCard title="Parent" description="For Parents and Guardians" url="/parent-register" />
      </SimpleGrid>
    </Container>

    </div>
  
  )
}

export default AuthWelcome