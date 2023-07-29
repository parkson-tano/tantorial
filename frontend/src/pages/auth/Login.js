import {
  TextInput,
  PasswordInput,
  Checkbox,
  Anchor,
  Paper,
  Title,
  Text,
  Container,
  Group,
  Button,
} from '@mantine/core';
import { Link } from 'react-router-dom';


export default function Login() {
  return (
    <div
      style={{
        backgroundImage: `url(https://app.gradely.co/auth/img/AuthBg.0d514f33.svg)`,
      }}
    >
      <Container size={520} my={40}>
        <Title
          align="center"
          sx={(theme) => ({ fontFamily: `Greycliff CF, ${theme.fontFamily}`, fontWeight: 900 })}
        >
          Welcome to Tantorial!
        </Title>
        <Text color="dimmed" size="sm" align="center" mt={5}>
          Do not have an account yet?{' '}
          <Link to="/signup-lander">
            Register
          </Link>
        </Text>

        <Paper withBorder shadow="md" p={30} mt={30} radius="md">
          <TextInput label="User ID/Email" placeholder="you@mantine.dev" required />
          <PasswordInput label="Password" placeholder="Your password" required mt="md" />
          <Group position="apart" mt="lg">
            <Checkbox label="Remember me" />
            <Link to="/forgot-password">Forgot password?</Link>
          </Group>
          <Button fullWidth mt="xl">
            Sign in
          </Button>
        </Paper>
      </Container>

    </div>

  );
}